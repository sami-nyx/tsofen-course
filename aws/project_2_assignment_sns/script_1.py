import boto3


def preHandle(toopicName):
    client=client = boto3.client('sns')


client = boto3.client('sns')
response = client.list_topics(
    
)
def create_topic(name):
    """
    Creates a notification topic.

    :param name: The name of the topic to create.
    :return: The newly created topic.
    """
    sns = boto3.resource("sns")
    topic = sns.create_topic(Name=name)
    return topic




def list_topics():
    """
    Lists topics for the current account.

    :return: An iterator that yields the topics.
    """
    sns = boto3.resource("sns")
    topics_iter = sns.topics.all()
    return topics_iter


def create_subscriptions(topicName):
    topics=list_topics()
    for topic in topics:
        if  topicName in topic.arn:
            print(topic.arn)
            subscription_iterator = topic.subscriptions.all()
            for subscription in subscription_iterator:
                print(subscription)
                subscription.delete()

            # subscription = topic.subscribe(
            #                 Protocol='email',
            # Endpoint='sami.a@moona.co',
            # Attributes={
            # },
            # ReturnSubscriptionArn=True
            # ) 
            # subscription = topic.subscribe(
            #                 Protocol='sms',
            # Endpoint='+972502702770',
            # Attributes={
            # },
            # ReturnSubscriptionArn=True
            # )           

            subscription = topic.subscribe(
                            Protocol='lambda',
            Endpoint='arn:aws:lambda:us-east-1:576374013711:function:myFunc',
            Attributes={
            },
            ReturnSubscriptionArn=True
            )           
# print(create_topic("byBoto3"))
print(create_subscriptions('myDemoConsoleTopic'))