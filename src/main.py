from random import randint

def fifo(pages,number_of_page_frames):
    frames =  []
    page_faults = 0
    for page in pages:
        if page not in frames:
            page_faults += 1
            if len(frames) >= number_of_page_frames:
                frames.pop(0)
            frames.append(page)
    return page_faults

def aging(number_of_page_frames, pages):
    frames = []
    ages = [0] * number_of_page_frames 
    page_faults = 0
    for page in pages:
        if page in frames:
            idx = frames.index(page)
            ages[idx] = (ages[idx] >> 1 | 0b10000000) 
        else:
            page_faults += 1
            if len(frames) < number_of_page_frames:
                frames.append(page)   
                ages[frames.index(page)] = 0b10000000


def generate_references(num_references, num_pages):
    return [randint(0, num_pages - 1) for _ in range(num_references)]


if __name__ == '__main__':
    number_of_page_frames = 5
    # pages = ['A', 'A', 'C', 'E', 'B', 'B', 'F', 'H', 'G', 'F','B', 'A', 'E', 'E', 'E', 'A', 'D', 'I', 'G', 'G']
    pages = generate_references(8, 4)
    print(pages)
    print(fifo(pages, number_of_page_frames))
    