# DDB - Installation

This section will provide a step-by-step guide to setting up the Digital Data Backbone. The installation process will include setting up the MQTT Broker, Cloud Databases, Event Listeners, and Retrieval Services. These components are explained in detail in the [Overview](DDB.md) section.


```{contents}
```

## Step 1: Broker Setup (Pub-Sub Broker Layer)

* Download the MQTT Broker Zip File and install in desired location.
* The MQTT Broker Link: <a>https://www.emqx.com/en/downloads/broker/v5.3.2</a><br/>
* Once installed navigate to the bin folder and start the broker by running the following command:

    ```
    cd emqx\bin
    emqx start
    ```

* Check if the broker is running by going to <a>http://localhost:18083/</a> in a web browser.
* Log in with the default username `admin` and password `public`
* Additional configurations can be done via the web portal.

## Step 2: Cloud Databases (Cloud Storage Layer)

### Aveva PI Historian
* The Aveva PI Historian requires a few different components, including PI Data Archive, PI Interface Server, PI Assett Framework Server, and PI Vision. Follow the installation guide below to install the components. \
<a>https://docs.aveva.com/bundle/pi-server-l-install/page/1020115.html</a><br><br>

* **Storage Connector**: MQTT Sparkplug B \
    The MQTT Sparkplug B connector is used to connect the MQTT Broker to the PI Historian. The connector is available in the link below:<br>
    <a>https://docs.aveva.com/bundle/pi-connector-for-mqtt-sparkplug/page/1010369.html</a>

### SQL

* Get a SQL Server
    * Setup on your local machine [(https://www.microsoft.com/en-us/sql-server/sql-server-downloads)](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

    * Or use a cloud service ([AWS](https://www.microsoft.com/en-us/sql-server/sql-server-downloads), [Azure](https://azure.microsoft.com/en-us/products/azure-sql), [Google Cloud](https://cloud.google.com/sql-server))

    *NOTE: We used an existing SQL Server on CMU campus cloud for our project.*

* Create a SQL database in a SQL server

    <a>https://learn.microsoft.com/en-us/sql/relational-databases/databases/create-a-database?view=sql-server-ver16</a>


* Create the following tables and stored procedures by executing the scripts below:\
<a href='https://github.com/cmu-mfi/dbb_interfaces/blob/main/retrieval/ProjectList.sql'>ProjectList<a></br>
<a href='https://github.com/cmu-mfi/dbb_interfaces/blob/main/retrieval/ExperimentList.sql'>ExperimentList</a></br></br>


* **Storage Connector**
    * SQL Store Procedures
        Create stored procedure by executing the scripts below:\
        <a href='https://github.com/cmu-mfi/dbb_interfaces/blob/main/from_mqtt/mqtt_sql/InsertXmlData.sql'>InsertXmlData</a></br></br>
        
        
    * XML to SQL \
        We use SQL to store XML data. A python script is used in `from_mqtt/mqtt_sql/XMLtoSQL` folder. The script reads the XML file and sends it to the stored procedure.


### Cloud File Storage
Partition a drive on a VM to create Cloud File storage. 

Connector: MQTT Msgs

## Step 4: Event Listeners

* Event listeners are basically converters that convert data from a local system message format to desired MQTT message format.
* The event listeners are available in the `to_mqtt` folder.
* An event listener is setup on a local machine which is both connected to the data generator source and the MQTT broker on the cloud network 
* Choose an event listener based on data generator source and run following commands:
    ```
    # Navigate to the event listener folder
    cd to_mqtt/<event_listener_name>

    # Setup virtual environment and install required libraries
    python -m venv ./.venv
    source .venv/bin/activate
    pip install -r requirements.txt

    # Command to start the event listener
    python scripts/mqtt_publisher.py
    ```
    *NOTE: commands may vary based on the event listener chosen. Follow steps in `to_mqtt/<event_listener_name>/README.md`*


## Step 5: Retrieval Services

* The retrieval service uses an HTML front-end and Flask Server back-end.
* Start the server by running the following commands:

    ```
    # Create Virtual Enviorment
    python -m venv ./.venv

    # Install Required Libraries
    pip install requirements.txt

    # Command to start the API
    python API/api.py
    ```

* Click on HTML file to start the UI

    ...

## System Checks and Troubleshooting

* 
* ...