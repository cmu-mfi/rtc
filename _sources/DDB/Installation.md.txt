# DDB - Installation

```{contents}
```

## Step 1: Broker Setup
Download the MQTT Broker Zip File and install in desired location.<br/>
The MQTT Broker Link: <a>https://www.emqx.com/en/downloads/broker/v5.3.2</a><br/>

```
cd emqx\bin
emqx start
```
Open your web browser<br/>
Go to <a>http://localhost:18083/</a> </br>
Log in with the default username "admin" and password "public"

## Step 2: Cloud Databases

### Aveva PI Historian
The Aveva PI Historian requires a few different components, including PI Data Archive, PI Interface Server, PI Assett Framework Server, and PI Vision.</br>
<a>https://docs.aveva.com/bundle/pi-server-l-install/page/1020115.html</a>


Connector: MQTT Sparkplug B</br>
<a>https://docs.aveva.com/bundle/pi-connector-for-mqtt-sparkplug/page/1010369.html</a>
### SQL
Create a SQL database in a SQL server.</br> 

Create the following tables by executing the scripts below:


Connector: Store Procedures
Create stored procedure by executing the scripts below:

### Cloud File Storage
Partition a drive on a VM to create Cloud File storage. 

Connector: MQTT Msgs

## Step 4: Event Listeners
...


## Step 5: Retrieval Services
The retrieval service uses an HTML front-end and Flask Server back-end. </br>

Create Virtual Enviorment:
```
python -m venv ./.venv
```
Install Required Libraries:
```
pip install requirements.txt
```
Command to start the API:</br>
```
python API/api.py
```
Click on HTML file to start the UI:


<hr>

## System Checks and Troubleshooting

* 
* ...