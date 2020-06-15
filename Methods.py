def rmtree_onerror(function, path, exec_info):
    '''
    Onerror Handeller for shutil.rmtree()
    Usage: 
    import shutil
    shutil.rmtree(filepath, onerror=rmtree_onerror)

    Resouce: https://stackoverflow.com/a/2656405/12468930
    '''
    import os 
    import stat

    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)

        function(path)
    

def export_vars(username, path):
    '''
    Writes a shell File with the Important Variable for commands.sh
    Example:

    export USERNAME='Value'
    export DIR='Value'
    '''
    import os

    with open(os.path.join(os.path.dirname(__file__), 'dataset/vars.sh'), 'w') as f:
        f.write(
            "export USERNAME=\"{}\"\nexport DIR=\"{}\"".format(username, path)
        )

export_vars('abdullahth', 'e:/Projects')