def readFile(arch, base=32):
    data = list()
    try:
        archive = open(arch, 'rt')
    except:
        print("Erro ao ler o arquivo! \nVerifique se o nome foi inserido corretamente.")
    else:
        for line in archive:
            val = line.strip("\n")
            if len(val) == base:
                data.append(val)
    finally:
        archive.close()
        return data
