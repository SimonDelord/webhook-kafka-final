from flask import Flask, request, jsonify
from kafka import KafkaProducer

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook_receiver():
    # Process the data and perform actions based on the event
    body = request.json
    print("Received webhook data:", body)
    return jsonify({'message': 'Webhook received successfully'}), 200

    #Bootstraps an instance of a Kafka producer.
    #Initializes the producer and identifies the docker server.
    #Sets the producer serializer to JSON
    producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    #Send a message to the kafka topic 'acs-topic'
    #passes the POST JSON body as the message
    producer.send('acs-topic', body)
    #Closes the TCP stream to Kafka
    producer.close()
    #Returns a Complete string
    return "Complete"
if __name__ == '__main__':
#    app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=8001)
