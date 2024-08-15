from random import choices

def fifo(pages, number_of_page_frames):
    frames = []
    page_faults = 0
    for page in pages:
        if page not in frames:
            page_faults += 1
            if len(frames) >= number_of_page_frames:
                frames.pop(0)
            frames.append(page)
    return page_faults

def aging(pages, number_of_page_frames):
    frames = []
    ages = [0] * number_of_page_frames
    page_faults = 0
    for page in pages:
        if page in frames:
            idx = frames.index(page)
            ages[idx] = (ages[idx] >> 1) | 0b10000000  # Coloca 1 no bit mais significativo e desloca para a direita
        else:
            page_faults += 1
            if len(frames) < number_of_page_frames:
                frames.append(page)
                ages[frames.index(page)] = 0b10000000  # Adiciona a nova página com idade inicial
            else:
                idx = ages.index(min(ages))
                frames[idx] = page
                ages[idx] = 0b10000000  # Reseta a idade da nova página
        # Atualiza as idades das páginas não referenciadas
        for i in range(len(frames)):
            if frames[i] != page:
                ages[i] = ages[i] >> 1  # Desloca para a direita
    return page_faults

def generate_references(num_references, num_pages):
    if num_references <= 0:
        raise ValueError("O número de referências deve ser maior que zero.")
    if num_pages <= 0:
        raise ValueError("O número de páginas deve ser maior que zero.")
    return choices(range(num_pages), k=num_references)

if __name__ == '__main__':
    number_of_page_frames = 3
    number_of_page = 8
    number_of_references = 34
    references = generate_references(number_of_references, number_of_page)
    print("FIFO Page Faults:", fifo(references, number_of_page_frames))
    print("Aging Page Faults:", aging(references, number_of_page_frames))
