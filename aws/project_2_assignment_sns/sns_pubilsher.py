import boto3

def get_sns():
    return boto3.resource("sns") 

def list_topics():
    """
    Lists topics for the current account.

    :return: An iterator that yields the topics.
    """
    sns = boto3.resource("sns")
    topics_iter = sns.topics.all()
    return topics_iter

def publish_message(topic, message):
    """
    Publishes a message to a topic.

    :param topic: The topic to publish to.
    :param message: The message to publish.
    :return: The ID of the message.
    """
    response = topic.publish(Message=message)
    message_id = response['MessageId']
    return message_id

def publish_times_by_topic(topic,times):
    for i in range(times):
        message="this is test message no."+str(i)
        publish_message(topic,message)



def publis_5_by_topic_name_contains(topicName):
    topics=list_topics()
    for topic in topics:
        if  topicName in topic.arn:
            print(topic.arn)
            publish_times_by_topic(topic,1)
            print(publish_message(topic,"this is sent by boto3 demo script"))



publis_5_by_topic_name_contains('myDemoConsoleTopic')