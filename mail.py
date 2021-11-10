import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header

from constant import FROM_ADDR, MAIL_PASSWORD, TO_ADDR, SMTP_SERVER, SEND_NAME

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(log_file, is_success):
    try:
        f = open(log_file)
    except Exception as e:
        print('cannot open file '+log_file)
        return False

    lines = f.read()
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER)
        # server.set_debuglevel(1)
        server.login(FROM_ADDR, MAIL_PASSWORD)
        msg = MIMEText(lines, 'plain', 'utf-8')
        msg['From'] = _format_addr(SEND_NAME + '<%s>' % FROM_ADDR)
        if is_success:
            subject = '自动打卡'+ 'success'
        else:
            subject = '自动打卡'+ 'failed'
        msg['Subject'] = Header(subject, 'utf-8').encode()
        server.sendmail(FROM_ADDR, [TO_ADDR], msg.as_string())
    except Exception as e:
        print('send mail failed!')
        print(e)
        return False
    return True


