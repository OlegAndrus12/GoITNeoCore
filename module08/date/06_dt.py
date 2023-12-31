from datetime import datetime, MINYEAR

d = datetime.now()
print(MINYEAR)
print(d.toordinal())
print(d.timestamp())

print(d.ctime())
print(d.isoformat(sep="T"))

day = d.toordinal()
iso = d.isoformat(sep="T")
sec = str(d.timestamp())

restore_d_form_day = datetime.fromordinal(day)
restore_d_form_iso = datetime.fromisoformat(iso)
restore_d_form_sec = datetime.fromtimestamp(float(sec))

print(restore_d_form_day)
print(restore_d_form_iso)
print(restore_d_form_sec)
