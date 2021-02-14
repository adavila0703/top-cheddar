from django.db import models

class TeamTable(models.Model):
    id = models.AutoField(primary_key=True)

class PlayerTable(models.Model):
    id = models.AutoField(primary_key=True)

class BasicStatsTable(models.Model):
    id = models.AutoField(primary_key=True)

class AdvancedStatsTable(models.Model):
    id = models.AutoField(primary_key=True)
