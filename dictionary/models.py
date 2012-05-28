from django.db import models, connection
import django.core.validators
import django.core.exceptions

class Item(models.Model):
    itemTitle = models.CharField(max_length=255)
    
    def getItemTitle(self):
	return self.itemTitle

    def updateTitle(self, newTitle):
	item = Item.objects.filter(pk = self.id).update(itemTitle = newTitle)

class User(models.Model):
    password = models.CharField(max_length=40)
    email = models.EmailField()
    username = models.CharField(max_length=40)
    userLevel = models.IntegerField()

    def getUserName(self):
	return self.username

    def validateEmail(self, email):
    	from django.core.validators import validate_email
	from django.core.exceptions import ValidationError
	try:
        	validate_email( email )
	        return True
    	except ValidationError:
        	return False

    def createUser(self, password,mail,uname):
	if not User.objects.get(username = uname):
		if (self.validateEmail(mail)) :
			user = User(username = uname, password = password, email = mail, userLevel = 0)
			user.save()
	else:
		return "User created once"

    def updatePassword(self, newPass):
	user = User.objects.filter(username = self.username).update(password = newPass)

    def updateEmail(self, newMail):
	user = User.objects.filter(username = self.username).update(email = newMail)
		
    def updateLevel(self, newLevel):
	user = User.objects.filter(username = self.username).update(userLevel = newLevel)

    def deleteUser(self):
	user = User.objects.filter(pk = self.id)
	user.delete()

class Entry(models.Model):
    date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=10000)
    itemId = models.ForeignKey(Item)
    userId = models.ForeignKey(User)

    def userEntries(self, userId):
	return Entry.objects.filter(userId_id = userId).all()

    def itemEntries(self, iId):
	return Entry.objects.filter(itemId_id = iId).all()

    def createEntry(self, eContent, itemId, userId):
	if not Entry.objects.filter(content = eContent):
		entry = Entry(content = eContent, itemId_id = itemId, userId_id = userId)
		entry.save()
	else:
		return "Same content"

    def updateContent(self, newContent):
	entry = Entry.objects.filter(pk = self.id).update(content = newContent)

    def deleteEntry(self):
	entry = Entry.objects.filter(pk = self.id)
	entry.delete()
