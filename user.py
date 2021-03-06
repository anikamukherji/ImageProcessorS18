import models
import datetime


def create_user(username):
    user = models.User(username, 0, 0, 0, 0,
                       [], [], [], [], [], [], [], [], [], [])
    user.image_original.append("None")
    user.image_contrast.append("None")
    user.image_log.append("None")
    user.image_hist.append("None")
    user.image_reverse.append("None")
    user.upload_time.append(datetime.datetime.now())
    user.hist_time.append(datetime.datetime.now())
    user.contrast_time.append(datetime.datetime.now())
    user.log_time.append(datetime.datetime.now())
    user.reverse_time.append(datetime.datetime.now())
    user.save()
    return user.vals()


def add_uploadimage(username, image, time):
    """
    store the information about the upload image
    """
    user = models.User.objects.raw({"_id": username}).first()
    user.image_original.append(image)
    user.upload_time.append(time)
    user.save()
    return user.vals()


def already_user(username):
    """
    Return whether user has already been created
    :param username: username of user
    :type username: string
    :returns: if user with username already exists
    :rtype: boolean
    """
    return models.User.objects.raw({"_id": username}).count() > 0


def add_image_hist(username, image, time):
    """
    store the information about the processed image which is using hist
    """
    user = models.User.objects.raw({"_id": username}).first()
    user.image_hist.append(image)
    user.hist_time.append(time)
    user.hist_times += 1
    user.save()
    return user.hist_times


def add_image_contrast(username, image, time):
    """
    store the information about the processed image which is using contrast
    """
    user = models.User.objects.raw({"_id": username}).first()
    user.image_contrast.append(image)
    user.contrast_time.append(time)
    user.contrast_times += 1
    user.save()
    return user.contrast_times


def add_image_log(username, image, time):
    """
    store the information about the processed image which is using log
    """
    user = models.User.objects.raw({"_id": username}).first()
    user.image_log.append(image)
    user.log_time.append(time)
    user.log_times += 1
    user.save()
    return user.log_times


def add_image_reverse(username, image, time):
    """
    store the information about the processed image which is using reverse
    """
    user = models.User.objects.raw({"_id": username}).first()
    user.image_reverse.append(image)
    user.reverse_time.append(time)
    user.reverse_times += 1
    user.save()
    return user.reverse_times
