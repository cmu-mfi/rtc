# Digital Data Backbone

*Overview*

```{contents}
```

*<diagram>*

## Layers

text

### Data Generators

### Event Listener

### Pub-Sub Broker

### Storage Connectors

### Cloud Storage

### Retrieval


## Software

<a href="https://github.com/cmu-mfi/dbb_interfaces.git" class="inline-button"><i class="fab fa-github"></i>dbb_interfaces</a>

The github repository is organized as shown below. `from_mqtt` has modules for various "Connectors" in the "Storage Connector" layer, and similarly `to_mqtt` has modules for "Event Listener" layer.


```
├───from_mqtt
│   ├───mqtt_cfs
│   ├───mqtt_pi
│   └───mqtt_sql
│       └───XMLtoSQL
└───to_mqtt
    ├───lfs_mqtt
    ├───ros_mqtt_cfs
    └───ros_mqtt_pi
```