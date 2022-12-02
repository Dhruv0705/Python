class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for directory in path.split("/"):
            if directory == ".":
                pass
            elif directory == "..":
                pass
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(directory)

        return "/" + "".join(stack)