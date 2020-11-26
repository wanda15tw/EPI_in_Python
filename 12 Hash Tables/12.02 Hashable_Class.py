class ContactList:
    def __init__(self, names):
        '''
        names is a list of strings
        :param names:
        '''
        self.names = names

    def __hash__(self):
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(other.names)


def merge_contact_lists(contacts):
    '''

    :param contacts: contacts is a list of ContactList
    :return:
    '''

    return list(set(contacts))