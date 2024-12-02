# Robot-Camera Calibration 

```{contents}
:maxdepth: 2
```

There are two types of robot-camera calibration:
* **eye-on-base**: camera is mounted on a fixed base
* **eye-on-hand**: camera is mounted on the robot


## Method: eye-on-base

<!-- <img src="../../../../files/vision/eye-on-base.png" alt="eye-on-base" width="400"/> -->

![eye-on-base](../../files/vision/eye-on-base.png)

| Known Value(s) | Collected Samples | Unknown Value(s) |
| --- | --- | --- |
| {math}`^gT_m` | {math}`^bT_g^{(i)}, ^cT_m^{(i)}` | {math}`^bT_c` |

Given a setup of camera on fixed base, the procedure to calibrate the robot-camera system is as follows:

1. Mount a marker on the robot end effector.
2. Estimate {math}`^gT_m`, the transformation matrix marker to gripper. \ 
    This value is determined from CAD reference *(preferred)* or measuring the marker center from end effector frame. If using ArUco marker, the marker center is the origin of the marker frame.
![aruco-frame](../../files/vision/aruco-frame.png)
<!-- <center><img src='../../../../files/vision/aruco-frame.png' alt='aruco-frame' width='250'/></center> -->

3. Collect samples of {math}`^bT_g^{(i)}` and {math}`^cT_m^{(i)}`. \
    Each sample is collected by moving the robot to a new pose and capturing the image of the marker. The pose of the marker in the image is used to estimate {math}`^cT_m^{(i)}`. The pose of the robot end effector is used to estimate {math}`^bT_g^{(i)}`.
4. Estimate {math}`^bT_c`, the transformation matrix base to camera using suitable algorithm as discussed in [section below](#calibration-algorithms). Following are the inputs to solve {math}`^bT_c`
> {math}`^bT_m^{(i)} \mid i = 1...n`: Transformation matrix marker to robot base. {math}`^bT_m^{(i)} = {^bT_g^{(i)}} \cdot {^gT_m} ` \
> {math}`^cT_m^{(i)} \mid i = 1...n`: Transformation matrix marker to camera.

5. Validate the calibration by checking the reprojection error, {math}`\epsilon`.
```{math}
    \epsilon = \frac{1}{n} \cdot {\sum_{i=1}^{n}{\lVert (^bT_c \cdot {^cT_m^{(i)}}) [:,3] - (^bT_m^{(i)})[:,3]\rVert}}
```

## Method: eye-on-hand

![eye-on-hand](../../files/vision/eye-on-hand.png)

| Known Value(s) | Collected Samples | Unknown Value(s) |
| --- | --- | --- |
| {math}`^bT_{c'}` | {math}`^bT_g^{(i)}, ^cT_m^{(i)}` | {math}`^gT_c` |

In this setup, we use one of the calibrated cameras fixed on base to calibrate a camera mounted on the robot end effector. The method is similar to eye-on-base calibration.

1. Put a marker such that it is fixed w.r.t. the robot base, and in view of both cameras ({math}`c'` and {math}`c`).
2. Using the eye-on-base calibration, we get {math}`^bT_m = {^bT_{c'}}\cdot{^{c'}T_m}`. The *eye-on-base* camera takes a picture of the marker and estimates {math}`^{c'}T_m`.
3. Collect samples of {math}`^bT_g^{(i)}` and {math}`^cT_m^{(i)}`. \
    Each sample is collected by moving the robot to a new pose and capturing the image of the marker. The pose of the marker in the image is used to estimate {math}`^cT_m^{(i)}`. The pose of the robot end effector is used to estimate {math}`^bT_g^{(i)}`.
4. Estimate {math}`^gT_c`, the transformation matrix base to camera using suitable algorithm as discussed in [section below](#calibration-algorithms). Following are the inputs to solve {math}`^gT_c`
> {math}`^gT_m^{(i)} \mid i = 1...n`: Transformation matrix marker to robot gripper. {math}`^gT_m^{(i)} = {(^bT_g^{(i)})^{-1}} \cdot {^bT_m} ` \
> {math}`^cT_m^{(i)} \mid i = 1...n`: Transformation matrix marker to camera.

5. Validate the calibration by checking the reprojection error, {math}`\epsilon`.
```{math}
    \epsilon = \frac{1}{n} \cdot {\sum_{i=1}^{n}{\lVert (^gT_c \cdot {^cT_m^{(i)}}) [:,3] - (^gT_m^{(i)})[:,3]\rVert}}
```

---

## Code Overview

![calibration-code](../../files/vision/calibration.png)

All the calibration related methods in above figure are in [`calibration/calibration.py`](https://github.com/cmu-mfi/rtc_vision_toolbox/blob/main_v2/calibration/calibrations.py). \
To collect samples, `collect_data` method takes three class objects as input: `robot`, `camera`, and `marker`. Each new robot type, camera type, or marker type needs its own class. Use existing classes as examples to create a new one, if needed.

* `robot` classes are in [/robot folder](https://github.com/cmu-mfi/rtc_vision_toolbox/tree/main_v2/robot)
* `camera` classes are in [/camera folder](https://github.com/cmu-mfi/rtc_vision_toolbox/tree/main_v2/camera)
* `marker` classes are in [/calibration/marker folder](https://github.com/cmu-mfi/rtc_vision_toolbox/tree/main_v2/calibration/marker)


**Usage**: Scripts, [`scripts/robot_camera_calibration.py`](https://github.com/cmu-mfi/rtc_vision_toolbox/blob/main_v2/scripts/robot_camera_calibration.py) and [`scripts/gripper_camera_calibration.py`](https://github.com/cmu-mfi/rtc_vision_toolbox/blob/main_v2/scripts/gripper_camera_calibration.py) can be used to execute the calibration method discussed above and show in the figure. 

---

## Useful Tips

- **Sample Collection**: Samples with high rotational variance and low translational variance have better calibration results. Adjust that in `calibartions.py` file.
- **Reprojection Error**: A low reprojection error indicates a good calibration. Error value <2mm is considered good.

---

## Calibration Algorithms

- **One Sample Estimate**  
  Calculate the following for each sample, and select the one with the best average reprojection error for the set.

```{math}
    ^bT_c^{(i)} = ^bT_m^{(i)} \cdot (^cT_m^{(i)})^{-1}
```

- **Kabsch-Umeyama algorithm**  
  The algorithm calculates the optimal rotation matrix that minimizes the root mean squared deviation between two paired sets of points [\[1\]](#references).

- **OpenCV Approach 1: Rotation then Translation**  
  In this approach, OpenCV provides the following methods to first estimate the rotation and then the translation (separable solutions):
  - R. Tsai, R. Lenz: *A New Technique for Fully Autonomous and Efficient 3D Robotics Hand/Eye Calibration* [\[2\]](#references)
  - F. Park, B. Martin: *Robot Sensor Calibration: Solving AX = XB on the Euclidean Group* [\[3\]](#references)
  - R. Horaud, F. Dornaika: *Hand-Eye Calibration* [\[4\]](#references)

- **OpenCV Approach 2: Simultaneous rotation and translation**  
  Another approach consists of estimating simultaneously the rotation and the translation (simultaneous solutions), with the following implemented methods:
  - N. Andreff, R. Horaud, B. Espiau: *On-line Hand-Eye Calibration* [\[5\]](#references)
  - K. Daniilidis: *Hand-Eye Calibration Using Dual Quaternions* [\[6\]](#references)

#### References
1. Lawrence, 2019. Purely Kabsch-Umeyama Algorithm.
2. Tsai, R., Lenz, R., 1989. A New Technique for Fully Autonomous and Efficient 3D Robotics Hand/Eye Calibration.
3. Park, F., Martin, B., 1994. Robot Sensor Calibration: Solving AX = XB on the Euclidean Group.
4. Horaud, R., Dornaika, F., 1995. Hand-Eye Calibration.
5. Andreff, N., Horaud, R., Espiau, B., 1999. On-line Hand-Eye Calibration.
6. Daniilidis, K., 1999. Hand-Eye Calibration Using Dual Quaternions.