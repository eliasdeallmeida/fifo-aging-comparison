import pandas as pd
from random import choices
from collections import deque

def fifo(pages, number_of_page_frames):
    """
    Implementa o algoritmo de substituição de páginas FIFO.
    
    Args:
    pages (list): Lista de referências de páginas.
    number_of_page_frames (int): Número de molduras de páginas disponíveis.
    
    Returns:
    int: Número de faltas de página.
    """
    frames = deque(maxlen=number_of_page_frames)
    page_faults = 0

    for page in pages:
        if page not in frames:
            page_faults += 1
            frames.append(page)
    return page_faults

def aging(pages, number_of_page_frames):
    """
    Implementa o algoritmo de substituição de páginas Aging.
    
    Args:
    pages (list): Lista de referências de páginas.
    number_of_page_frames (int): Número de molduras de páginas disponíveis.
    
    Returns:
    int: Número de faltas de página.
    """
    frames = []
    ages = [0] * number_of_page_frames
    page_faults = 0

    for page in pages:
        if page in frames:
            idx = frames.index(page)
            ages[idx] = (ages[idx] >> 1) | 0b10000000
        else:
            page_faults += 1
            if len(frames) < number_of_page_frames:
                frames.append(page)
                ages[frames.index(page)] = 0b10000000
            else:
                idx = ages.index(min(ages))
                frames[idx] = page
                ages[idx] = 0b10000000
        for i in range(len(frames)):
            if frames[i] != page:
                ages[i] = ages[i] >> 1
    return page_faults

def generate_references(num_references, num_pages):
    """
    Gera uma lista de referências de páginas aleatórias.
    
    Args:
    num_references (int): Número de referências a serem geradas.
    num_pages (int): Número total de páginas possíveis.
    
    Returns:
    list: Lista de referências de páginas.
    """
    if num_references <= 0:
        raise ValueError("O número de referências deve ser maior que zero.")
    if num_pages <= 0:
        raise ValueError("O número de páginas deve ser maior que zero.")
    return choices(range(num_pages), k=num_references)

def save_references_to_file(references, filename):
    """
    Salva a lista de referências de páginas em um arquivo.
    
    Args:
    references (list): Lista de referências de páginas.
    filename (str): Nome do arquivo onde as referências serão salvas.
    """
    with open(filename, 'w') as file:
        for ref in references:
            file.write(f"{ref}\n")

def compare_algorithms(num_references, num_pages, page_frames_list):
    """
    Compara os algoritmos FIFO e Aging para diferentes números de molduras de páginas.
    
    Args:
    num_references (int): Número de referências de páginas.
    num_pages (int): Número total de páginas possíveis.
    page_frames_list (list): Lista com diferentes números de molduras de páginas a serem testados.
    
    Returns:
    list: Lista de tuplas contendo o número de molduras de páginas, faltas de página para FIFO e faltas de página para Aging.
    """
    references = generate_references(num_references, num_pages)
    save_references_to_file(references, f"references{num_pages}.txt")

    results = []
    for frames in page_frames_list:
        fifo_faults = fifo(references, frames)
        aging_faults = aging(references, frames)
        results.append((frames, fifo_faults, aging_faults))

    return results

if __name__ == '__main__':
    print('rodou')
    num_references = 1000
    num_pages = [150, 300, 450, 600]
    # page_frames_list = [5, 10, 25, 30, 35, 40, 45, 50]
    page_frames_list = list(range(1, 151))
    # print(page_frames_list)

    # print(aging([2,4,5,2,4],3))

    '''
    2 144  1001 0000
    4 64 32  1001 0000
    5 128 32
    '''
    results = {}
    for page in num_pages:
        # print(page)
        # print("Número de Molduras | Faltas FIFO | Faltas Aging")
        results[page] = compare_algorithms(num_references, page, page_frames_list)
        # for frames, fifo_faults, aging_faults in results[page]:
        #     print(f"{frames:<18} | {fifo_faults:<11} | {aging_faults:<12}")
    
    for key, values in results.items():
        df = pd.DataFrame(values, columns=['Frame', 'fifo_faults', 'aging_faults'])
        df.to_csv(f'results{key}.csv', index=False)