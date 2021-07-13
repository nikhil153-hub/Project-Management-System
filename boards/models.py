from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from accounts.models import User


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=50, null=True, )
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
#
#     # def save(self, commit=True, *args, **kwargs):
#     #     # print("test: ", self)
#     #     request = None
#     #     # if kwargs.has_key('request'):
#     #     #     request = kwargs.pop('request')
#     #
#     #     print("request: ", kwargs)
#     #     # raise Exception('Upgrade to premium for more board!')
#     #     # raise ValidationError('The pools are all full.')
#     #
#     #     return super(Board, self).save()
#     #     if False:
#     #         pass
#     #     return None
#
#
# # @receiver(pre_save, sender=Board)
# # def board_limit(sender, **kwargs):
# #     print("test: ", kwargs)
# #     if True:
# #         raise Exception('Dont save me!')


class BoardList(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, )
    title = models.CharField(max_length=50, null=True, )
    sequence = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    board_list = models.ForeignKey(BoardList, on_delete=models.CASCADE, )
    title = models.CharField(max_length=50, null=True, )
    discription = models.TextField(null=True, )
    due_date = models.DateTimeField()
    sequence = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
