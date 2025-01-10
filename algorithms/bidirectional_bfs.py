from collections import deque

def word_ladder_bidirectional_bfs(begin_word, end_word, word_list):

    if end_word not in word_list:
        return 0

    word_list = set(word_list)
    word_list.add(begin_word)

    begin_queue = deque([(begin_word, 1)])
    end_queue = deque([(end_word, 1)])

    begin_visited = {begin_word: 1}
    end_visited = {end_word: 1}

    while begin_queue and end_queue:
        result = bfs_step(begin_queue, begin_visited, end_visited, word_list)
        if result:
            return result

        result = bfs_step(end_queue, end_visited, begin_visited, word_list)
        if result:
            return result

    return 0

def bfs_step(queue, visited, other_visited, word_list):

    current_word, level = queue.popleft()

    for i in range(len(current_word)):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            transformed_word = current_word[:i] + char + current_word[i+1:]

            if transformed_word in word_list:
                if transformed_word in other_visited:
                    return level + other_visited[transformed_word]

                if transformed_word not in visited:
                    visited[transformed_word] = level + 1
                    queue.append((transformed_word, level + 1))

    return None

if __name__ == "__main__":
    
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

    print("Words in word list: ")

    for word in word_list:
        print(word)

    begin_word = "hit"
    end_word = "cog"

    result = word_ladder_bidirectional_bfs(begin_word, end_word, word_list)
    
    if result:
        print(f"The shortest transformation sequence length is: {result}")
    else:
        print("No valid transformation sequence exists.")