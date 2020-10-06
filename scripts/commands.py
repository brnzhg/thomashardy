import db.testdb as tdb
import configparser
from pathlib import Path
import sqlalchemy as sa
from enum import Enum


config_filepath = Path(__file__).parent.parent.joinpath('config.ini').absolute()

config = configparser.ConfigParser()
config.read(config_filepath)
db_path = config['DEFAULT']['db_path']

# TODO need to check cascade rules

# view word
#   display everything, including synonyms (with s numbers?, further commands could be to look at one of them)

# edit word
#   allow word to be omitted, know what's editing based on last command
#   or last thing that has matching editable field

# edit
# word, tons of fields
# user word score, user word notes
# synonym word score, synonym word notes
# so all begin with edit word [-user/-synonym] colname
# 
# adding word, user, synonym, source, tag
#  

# maybe we just want data on requests and responses
# view word response linked to data of synonym requests
# request types need key or something?

# maybe this linking thing is too complicated... just have shortcuts for words (view .s1, view syn .s1)


# class ViewWordField(Enum):

class ViewWordRequest():

    def __init__(self, word_name, user_name, show_user_notes):
        self.word_name = word_name
        self.user_name = user_name
        self.show_user_notes = show_user_notes


class AddWordRequest():
    
    def __init__(self, word_name, user_name, definition, synonyms, tags):
        self.word_name = word_name
        self.user_name = user_name
        self.definition = definition
        self.synonyms = synonyms
        self.tags = tags


class EditWordRequest():
    pass

class DeleteWordRequest():
    pass


class ViewWordRequestOptions():

    def choose_request(self, word_option_key):
        return ViewWordRequest(self.word_options[word_option_key]
                              , self.user_name
                              , self.show_user_notes)
    
    def __init__(self, word_options, user_name, show_user_notes):
        self.word_options = word_options
        self.user_name = user_name
        self.show_user_notes = show_user_notes

# if they mispell synonym this can be relauncehed, or maybe unify with add word synonym
# maybe add word synonym, add word tag, all unified under add word
class AddWordRequestOptions():

    def choose_request(self, definition_keys):
        return 

    # TODO flesh out later with shortdef longdef
    def __init__(self, word_name, user_name, definition_options, synonyms, tags):
        self.word_name = word_name
        self.user_name = user_name
        self.definition_options = definition_options
        self.synonyms = synonyms
        self.tags = tags


class AddWordResponse():

    # should be interpeted as going through each unknown request, one after the other, can be cancelled (the cancel whole thing)
    def __init__(self
                , added_word
                , unknown_view_word_request
                , unknown_view_synonym_request
                , unknown_view_tag_request): # no options, if word is typo view word will figure it out, then link back to add word
        self.added_word = added_word

        self.unknown_view_word_request = unknown_view_word_request
        self.unknown_view_synonym_request = unknown_view_word_request
        self.unknown_view_tag_request = unknown_view_tag_request


#TODO do sources later
class ViewWordResponse():

    def __init__(self
                , word_vars
                , synonym_vars
                # , source_vars
                , tag_vars
                , retrieved_word # if hit an existing word, all good
                , add_new_word_request_options # if new word (spelled right) just call add new word, but otherwise show definitions and make options to add
                , unknown_view_word_request_options): # if wtf is this, have option of viewing fuzzy matches (which can lead to add or not, recursive)
        self.word_vars = word_vars
        self.synonym_vars = synonym_vars
        # self.source_vars = source_vars
        self.tag_vars = tag_vars

        self.retrieved_word = retrieved_word

        self.add_new_word_request_options = add_new_word_request_options
        self.unknown_view_word_request_options = unknown_view_word_request_options

    # consider ViewWordRetrievedResponse, same with others    

# mirrors ViewWord, ViewSynonym

# didnt make request since it mirros, whatever
class ViewSynonymResponse():
    
    def __init__(self
                , word_vars
                , synonym_vars
                , retrieved_synonym
                , add_new_word_synonym_request # not options, we don't need definitions, just pick from list of unknowns if not spell_check
                , unknown_view_synonym_request_options # list of spell checker suggestions
                ):
        self.word_vars = word_vars
        self.synonym_vars = synonym_vars

        self.retrieved_synonym = retrieved_synonym

        self.add_new_word_synonym_request = add_new_word_synonym_request
        self.unknown_view_synonym_request_options = unknown_view_synonym_request_options
#last thing to really figure out is edit 



# anytime unknown, go back to view word request options