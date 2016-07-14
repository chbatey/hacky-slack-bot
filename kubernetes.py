from slackbot.bot import respond_to
from slackbot.bot import listen_to
import subprocess

@listen_to('k8 nodes ([a-z,\-]*)')
def k8_nodes(message, context):
    output = subprocess.check_output(["kubectl", "get", "nodes",
        "--context", context]) 
    message.reply(output)

@listen_to('k8 pods ([a-z,\-]*)$')
def k8_pods(message, context):  
    output = subprocess.check_output(["kubectl", "get", "pods",
        "--context", context])
    message.reply(output)

@listen_to('k8 pods ([a-z,\-]*) ([a-z,\-]*)$')
def k8_pods(message, context, namespace):  
    output = subprocess.check_output(["kubectl", "get", "pods",
        "--context", context, "--namespace", namespace])
    message.reply(output)

@listen_to('k8 describe ([a-z,\-]*) ([a-z,\-]*)$')
def k8_describe(message, context, pod_name):
    output = subprocess.check_output(["kubectl", "describe",
        "--context", context, "--namespace", "default", "pod", pod_name])
    message.reply(output)
