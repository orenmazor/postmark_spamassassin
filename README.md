### Requirements

You'll need a copy of Requests, which is fantastic: http://docs.python-requests.org/en/latest/index.html, and a moderately recent version of python (at least above 2.5)

### Usage

`from spamcheck import spamcheck`

create an instance:

`spamchecker = spamcheck.SpamCheck()`

now have some fun:

`spamchecker.GetScore("foo")`

`spamchecker.GetReport("foo")`

### Error Handling

 - Requests will throw an HTTPError on all status codes other than OK. these are propagated to you, brave adventurer.
 - The above library will throw a general Exception in any situation where SpamCheck returns an error. The message of the exception will be the error.

