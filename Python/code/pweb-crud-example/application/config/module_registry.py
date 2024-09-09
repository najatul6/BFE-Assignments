from pweb import PWebModuleRegister
from boot.boot_module import BootModule
from pweb_ssr.pweb_ssr_module import PWebSSRModule


class Register(PWebModuleRegister):

    def get_module_list(self) -> list:
        return [BootModule, PWebSSRModule]
