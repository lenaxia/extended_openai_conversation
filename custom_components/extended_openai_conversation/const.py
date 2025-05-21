"""Constants for the Extended OpenAI Conversation integration."""

DOMAIN = "extended_openai_conversation"
DEFAULT_NAME = "Extended OpenAI Conversation"
CONF_ORGANIZATION = "organization"
CONF_BASE_URL = "base_url"
DEFAULT_CONF_BASE_URL = "https://api.openai.com/v1"
CONF_API_VERSION = "api_version"
CONF_SKIP_AUTHENTICATION = "skip_authentication"
DEFAULT_SKIP_AUTHENTICATION = False

EVENT_AUTOMATION_REGISTERED = "automation_registered_via_extended_openai_conversation"
EVENT_CONVERSATION_FINISHED = "extended_openai_conversation.conversation.finished"

CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """The Current Time is: {{now()}}, if you are asked about it, format it in human readable format

Available Devices:
```csv
entity_id,name,state,aliases,supports_brightness,brightness
{% for entity in exposed_entities -%}
  {%- set supports_brightness = 'No' -%}
  {%- set brightness = 'N/A' -%}
  {%- if 'supported_color_modes' in entity.attributes -%}
    {%- if 'brightness' in entity.attributes.supported_color_modes -%}
      {%- set supports_brightness = 'Yes' -%}
      {%- if entity.state == 'on' -%}
        {%- if 'brightness' in entity.attributes -%}
          {%- set brightness = entity.attributes.brightness %}
        {%- else -%}
          {%- set brightness = 'N/A' %}
        {%- endif -%}
      {%- else -%}
        {%- set brightness = '0' %}
      {%- endif -%}
    {%- endif -%}
  {%- endif -%}
{{ entity.entity_id }},{{ entity.name }},{{ entity.state }},{{entity.aliases | join('/') }},{{ supports_brightness }},{{ brightness }}
{% endfor %}
```

You are a mildly sarcastic personal assistant who is responsible for managing a smart home powered by Home Assistant. Based only on knowledge you know is factual, you will answer any question or act on any request that a user asks you. `Available Devices` is a list of devices that you can control in the smart home.

For any request that you receive, first identify the intent by answering the following question:

Is the user requesting information/status or is the user requesting you to take an action?

If the user is requesting information or a status update about something you know (e.g. the state of a light or door), provide the answer and end your response. A request for information may also take the form of a conversation, such as asking about the weather, how you're feeling, asking for a joke, whether someone is home, or anything else along these lines. Do not make any function calls if information is being requested. If asked about any time or date related information, make sure to respond in a human readable format.

If you determine the intent of the user is to ask you to perform an action, you can do so by using the `execute_services` function call. Be sure to properly fill out any function parameters using the `Availalbe Devices` list above or your previous knowledge of Home Assistant features. Do not leave any parameter undefined or in a default value. If you don't have enough information to execute a function call or smart home command, specify what other information you need. When changing the state of a light, always define a bightness level in the attributes
"""
CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = "gpt-4o-mini"
CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 150
CONF_TOP_P = "top_p"
DEFAULT_TOP_P = 1
CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.5
CONF_MAX_FUNCTION_CALLS_PER_CONVERSATION = "max_function_calls_per_conversation"
DEFAULT_MAX_FUNCTION_CALLS_PER_CONVERSATION = 1
CONF_FUNCTIONS = "functions"
DEFAULT_CONF_FUNCTIONS = [
    {
        "spec": {
            "name": "execute_services",
            "description": "Use this function to execute service of devices in Home Assistant.",
            "parameters": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "domain": {
                                    "type": "string",
                                    "description": "The domain of the service, which is part of the entity_id, e.g. light.kitchen_lights has a domain of lights, and binary_sensor.fridge_door has a domain of binary_sensor",
                                },
                                "service": {
                                    "type": "string",
                                    "description": "The service to be called",
                                },
                                "service_data": {
                                    "type": "object",
                                    "description": "The service data object to indicate what to control.",
                                    "properties": {
                                        "brightness": {
                                            "type": "integer",
                                            "description": "Controls how bright a light wll be. 255 is 100%, 128 is 50%, 0 is 0%.",
                                        },
                                        "entity_id": {
                                            "type": "string",
                                            "description": "The entity_id retrieved from available devices. It must start with domain, followed by dot character.",
                                        }
                                    },
                                    "required": ["entity_id"],
                                },
                            },
                            "required": ["domain", "service", "service_data"],
                        },
                    }
                },
            },
        },
        "function": {"type": "native", "name": "execute_service"},
    }
]
CONF_ATTACH_USERNAME = "attach_username"
DEFAULT_ATTACH_USERNAME = False
CONF_USE_TOOLS = "use_tools"
DEFAULT_USE_TOOLS = False
CONF_CONTEXT_THRESHOLD = "context_threshold"
DEFAULT_CONTEXT_THRESHOLD = 13000
CONTEXT_TRUNCATE_STRATEGIES = [{"key": "clear", "label": "Clear All Messages"}]
CONF_CONTEXT_TRUNCATE_STRATEGY = "context_truncate_strategy"
DEFAULT_CONTEXT_TRUNCATE_STRATEGY = CONTEXT_TRUNCATE_STRATEGIES[0]["key"]

SERVICE_QUERY_IMAGE = "query_image"

CONF_PAYLOAD_TEMPLATE = "payload_template"
