# Create a .txt file that contains my favorite poem
file_content = "Sometimes with one I love I fill myself with rage for fear I effuse unreturn’d love, But now I think there is no unreturn’d love, the pay is certain one way or another, (I loved a certain person ardently and my love was not return’d, Yet out of that I have written these songs.)"
poem_file = open('poem_Yu.txt', 'wt', encoding = 'utf-8')
poem_file.write(file_content)
poem_file.close()

# Add a line of text including the poet
poem_file = open('poem_Yu.txt', 'at')
poem_file.write("\n--Written by Walt Whitman, 1819 - 1892")
poem_file.close()


# Use the while. for method to open the file and print each line of your file
with open('poem_Yu.txt', 'rt', encoding = 'utf-8') as file:
    for line in file:
        print(line)

# Use list comprehension to print each line of the poem
line_list = [line.split('\n') for line in open ('poem_Yu.txt', encoding = 'utf-8')]

        
