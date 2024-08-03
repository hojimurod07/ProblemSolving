def process_likes_dislikes(actions):
    stack = []
    i = 0
    while i < len(actions):
        if actions[i:i + 4] == "Like":
            if stack and stack[-1] == "Like":
                stack.pop()  # Cancel out with the previous Like
            else:
                stack.append("Like")
            i += 4  # Move the index to skip the current "Like"
        elif actions[i:i + 7] == "Dislike":
            if stack and stack[-1] == "Dislike":
                stack.pop()  # Cancel out with the previous Dislike
            elif stack and stack[-1] == "Like":
                stack.pop()  # Dislike cancels out a previous Like
            else:
                stack.append("Dislike")
            i += 7  # Move the index to skip the current "Dislike"
        else:
            i += 1  # Move forward if no valid action is found

    return stack[-1] if stack else "Nothing"


# Examples
print(process_likes_dislikes("Dislike"))  # Output: "Dislike"
print(process_likes_dislikes("LikeLike"))  # Output: "Nothing"
print(process_likes_dislikes("DislikeLike"))  # Output: "Like"
