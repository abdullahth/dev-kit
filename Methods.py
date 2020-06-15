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
    

