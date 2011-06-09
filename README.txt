django-cookie-sessions
======================

This is a session backend which uses Django's secure cookie encoding and
decoding functionality to store the whole session in the cookie, instead of
talking to some database or cache instance.

Installation
------------

Set this in your settings:

    SESSION_ENGINE = 'cookiesessions.engine'

Why would I want this?
----------------------

With all of the other Django session backends every request from a user results
in a request to some backend service, whether it be a database, memcached, or
something else.  Wouldn't it be better if we could store that information with
the client itself, and save ourselves the extra requests and latency?

Prior to Django 1.4, it was not possible, because you couldn't trust the user's
cookie.  Someone could have set their user_id in the cookie to someone else's,
and suddenly be logged in as that other user.  Thankfully Django 1.4 supports
securely signed cookies, meaning that we can ensure that the cookie was set by
us, and only us.

Given that, it's now possible to save ourselves these extra requests and
latency, as well as retain the strong security that we have come to expect
from web services built on Django.