
from django.contrib import admin
from .models import ConversationMessage, Conversation


admin.site.register(Conversation)
admin.site.register(ConversationMessage)
