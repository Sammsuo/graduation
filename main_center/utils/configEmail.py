# coding:utf-8

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import threading
from main_center.utils import readConfig
import zipfile
import glob
from main_center.utils import common

localReadConfig = readConfig.ReadConfig()


class Email:
    def __init__(self):
        global host, user, password, port, sender, title
        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_password")
        port = localReadConfig.get_email("mail_port")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_email("subject")

        # 获取接收者名单
        self.value = localReadConfig.get_email('receiver')  # TODO
        self.receiver = []
        for n in str(self.receiver).split(';'):
            self.receiver.append(n)

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 将时间返回str

        self.subject = title + '' + date

        # self.log = MyLog.get_log()
        # self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('related')  # 构造带附件的邮件

    def config_header(self):
        """
        定义邮件头 subject | from | to
        :return:
        """
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ';'.join(self.receiver)

    def congfig_content(self):
        """
        定义 邮件 内容
        :return:
        """
        f = open(os.path.join(readConfig.proDir, 'testFile', 'emailStyle.txt')) # 设置邮件模板
        content = f.read()
        f.close
        content_plain = MIMEText(content, 'html', 'UTF-8')
        self.msg.attach(content_plain)

    def config_image(self):  #  大概率用不上
        """
        定义能够用到的图片
        :return:
        """
        pass

    def config_file(self):
        """
        定义邮件文件
        :return:
        """
        if self.check_file():

            resultpath = common.get_result_path()
            zippath = os.path.join(readConfig.proDir, 'result', 'test.zip')

            # zip file
            files = glob.glob(resultpath + '\*')  # TODO
            f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
            for file in files:
                #修改压缩文件的目录结构
                f.write(file, '/report/' + os.path.basename(file))
            f.close()

            reportfile = open(zippath, 'rb').read()
            filehtml = MIMEText(reportfile, 'base64', 'utf-8')
            filehtml['Content-type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = "attachment; filename='test.zip'"
            self.msg.attach(filehtml)

    def check_file(self):
        """
        检查测试报告
        :return:
        """
        reportpath = common.get_report_path()
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:  # 检查testCase内是否有
            return True
        else:
            return False


    def send_email(self):
        """
        发送邮件
        :return:
        """
        self.config_header()
        self.congfig_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())  # TODO
            smtp.quit()
            print("邮件已发送")
        except Exception as e:
            print(e)


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == '__main__':
    c = MyEmail.get_email()
    print(c.msg)