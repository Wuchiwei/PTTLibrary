
import sys


class Language(object):

    zh_TW = 1
    en_US = 2

    _MinValue = zh_TW
    _MaxValue = en_US
    _BuffList = []

    log_debug = None
    log_warning = None
    log_info = None
    log_error = None
    log_fatal = None

    def __init__(self, language=0):
        self._BuffList = []
        LanguageSetting = 0

        if language == 0:
            LanguageSetting = self.zh_TW
        else:
            if not self._MinValue <= language <= self._MaxValue:
                print('Language init error')
                return
            LanguageSetting = language

        if LanguageSetting == self.zh_TW:
            self.log_debug = '除錯'
            self.log_warning = '警告'
            self.log_info = '資訊'
            self.log_error = '錯誤'
            self.log_fatal = '致命錯誤'
        elif LanguageSetting == self.en_US:
            self.log_debug = 'debug'
            self.log_warning = 'warning'
            self.log_info = 'info'
            self.log_error = 'error'
            self.log_fatal = 'fatal'
        
        self._BuffList.append(('log_debug', self.log_debug))
        self._BuffList.append(('log_warning', self.log_warning))
        self._BuffList.append(('log_info', self.log_info))
        self._BuffList.append(('log_error', self.log_error))
        self._BuffList.append(('log_fatal', self.log_fatal))

    def show(self):
        for name, value in self._BuffList:
            print(name.title() + ': ' + value)


if __name__ == '__main__':

    print('=' * 20 + ' Default ' + '=' * 20)

    default = Language()
    default.show()

    print('=' * 20 + ' zh_TW ' + '=' * 20)

    zh_TW = Language(Language.zh_TW)
    zh_TW.show()

    print('=' * 20 + ' en_US ' + '=' * 20)

    en_US = Language(Language.en_US)
    en_US.show()