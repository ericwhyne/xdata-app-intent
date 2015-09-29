#!/usr/bin/python
print "Starting Intent API"
from flask import Flask, jsonify, abort, request, send_from_directory
import sys
import yaml
import re

api_ver = 'v1.0'

#config_filename = sys.argv[1]
config_filename = "config.yaml"
try:
    config = yaml.safe_load(open(config_filename))
except:
    print "Failed to load config file ", config_filename
    exit(0)

app = Flask(__name__)

@app.route('/')
def index():
    return "Application Intents API " + api_ver + " using config file " + config_filename + "\n"

@app.route("/api/" + api_ver + "/intent", methods=['GET'])
def random_mumble():
    intent_type = request.args.get('type')
    if intent_type in config:
        ret = ''
        for app in config[intent_type]['applications'].keys():
            app_url = config[intent_type]['applications'][app]['call_url']
            for input_field in config[intent_type]['input'].keys():
                try:
                    app_url = re.sub(config[intent_type]['input'][input_field], request.args.get(input_field), app_url)
                except:
                    ret += "Error: " + app + " intent missing parameter " + input_field

            ret += "<a href=\"" + app_url + "\">" + app_url + "</a>"
            ret += "<img src=\"" + config[intent_type]['applications'][app]['icon'] + "\" height=50><br>"
        return ret
    else:
        return "<h3>Intent type " + str(intent_type)+ " not found.<h3>"

@app.route('/icons/<path:path>')
def send_icons(path):
    return send_from_directory('icons', path)

@app.route("/api/" + api_ver + "/discovery", methods=['GET'])
def return_config():
    return jsonify(config)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
