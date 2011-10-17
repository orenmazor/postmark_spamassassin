from spamcheck import spamcheck

spamchecker = spamcheck.SpamCheck()
print spamchecker.GetScore("foo")

print spamchecker.GetReport("foo")

