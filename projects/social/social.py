import random
from string import ascii_lowercase
from collections import deque


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[
                user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # automatically increment the ID to assign the new user
        self.last_id += 1
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of
        friendships.
        """
        if num_users <= avg_friendships:
            raise ValueError(
                'Number of users must be greater than average friendships')
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            name = ''.join(random.choice(ascii_lowercase) for i in range(8))
            self.add_user(name)

        # This is linear only if num_users >>> avg_friendships
        # Otherwise it spends all it's time trying to randomly generate
        # last few available friendships
        # Create friendships
        # Need to divide by 2 to account for bidirectional nature of graph
        total_friendships = num_users * avg_friendships // 2
        friendships_to_add = set()
        while len(friendships_to_add) < total_friendships:
            # Have to add 1 because user ids start from 1 not 0
            user_id = random.randrange(num_users) + 1
            friend_id = random.randrange(num_users) + 1
            if user_id == friend_id:
                continue
            if user_id > friend_id:
                user_id, friend_id = friend_id, user_id
            if (user_id, friend_id) not in friendships_to_add:
                friendships_to_add.add((user_id, friend_id))
        for friendship in friendships_to_add:
            self.add_friendship(*friendship)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = deque()
        queue.append((user_id, [user_id]))
        while len(queue) > 0:
            current_user, path = queue.popleft()
            if current_user in visited:
                pass
            else:
                visited[current_user] = path
                friends = self.friendships[current_user]
                for friend in friends:
                    new_path = path.copy()
                    new_path.append(friend)
                    queue.append((friend, new_path))
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    sg.populate_graph(1000, 5)

    total_connections = 0
    sample_size = 10
    for user in range(1, 1 + sample_size):
        connections = sg.get_all_social_paths(user)
        total_connections += len(connections)

    network_percentage = (total_connections / sample_size) / 10
    print('Network Percentage: ', network_percentage)
