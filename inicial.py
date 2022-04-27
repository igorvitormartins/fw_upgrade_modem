import configparser

config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')

def data_inicial():
    
    #obtendo dados do ini
    ip_dut = config.get("DATA","ip_dut")
    ip_dut_second = config.get("DATA","ip_dut_second")
    fw_version = config.get("DATA","fw_version")
    machead = config.get("DATA","machead")
    lastdigit = config.get("DATA","lastdigit")
    return ip_dut, ip_dut_second, fw_version, machead, lastdigit

def dir():
    
    diretorio_log = config.get("FILE_DATA","diretorio_log")
    return diretorio_log
