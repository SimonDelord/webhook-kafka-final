from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)
#@app.route('/webhook', methods=['POST'])
@app.route('/', methods=['POST'])

def hello(): #hello() is registered to route /
    #Gets the POST body as a JSON object
    print request.json
    body = request.json

    #Bootstraps an instance of a Kafka producer.
    #Initializes the producer and identifies the docker server.
    #kafka-spotify is listed in /etc/hosts with the ip of the container
    #Sets the producer serializer to JSON
    producer = KafkaProducer(bootstrap_servers='172.30.2.176:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    #Send a message to the kafka topic 'test'
    #passes the POST JSON body as the message
    producer.send('acs-topic', body)
    #Closes the TCP stream to Kafka
    producer.close()
    #Returns a Complete string
    return "Complete"
    
#producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#producer = KafkaProducer(bootstrap_servers='172.30.2.176:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#producer = KafkaProducer(bootstrap_servers='172.30.2.176:9092',value_serializer=lambda m: json.dumps(m).encode('ascii'))

if __name__ == '__main__':
#    app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=8001)
   
