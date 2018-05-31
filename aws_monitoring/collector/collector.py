from six.moves import configparser
import importlib

def main():
    ext_path = "aws_monitoring.extensions." 
    conf_file = "aws_monitor.ini"
    config = configparser.ConfigParser()
    config.read(conf_file)
    modules = config.get('extensions', 'resources')
    print("Modules list: %s" % modules)
    mod_list = modules.split(",")

    for mod in mod_list:
        module = importlib.import_module(ext_path + mod)
        mod_class = getattr(module, mod)
        mod_inst = mod_class()
        mod_inst.initialize()
        resp = mod_inst.run()
        print("%s: %s" % (mod, resp))
     
  
if __name__== "__main__":
    main()
