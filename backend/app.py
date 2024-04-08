from flask import Flask
from api.kafka_consumer import kafka_consumer   # Import the blueprint from the kafka_consumer module

app = Flask(__name__)

# Register the Kafka consumer blueprint
app.register_blueprint(kafka_consumer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
