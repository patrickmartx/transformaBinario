def readFile(arch, base=32):
    '''
    :param arch: Nome do arquivo a ser lido.
    :return: Lista de ítens encontrados no arquivo separado por linhas.
    '''
    data = list()
    try:
        archive = open(arch, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        for line in archive:
            val = line.strip("\n")
            if len(val) == base:
                data.append(val)
    finally:
        archive.close()
        return data
