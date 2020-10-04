from sqlalchemy import String, Table, Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)


class VocabWord(Base):
    __tablename__ = 'vocabwords'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class VocabDefinition(Base):
    __tablename__ = 'vocabdefinitions'
    id = Column(Integer, ForeignKey(VocabWord.id), primary_key=True)
    short_def = Column(String)
    long_def = Column(String)
    
    example = Column(String)
    notes = Column(String)

    # user_score = Column(Integer)
    # recognize_count = Column(Integer)
    # miss_count = Column(Integer)

    vocab_word = relationship("VocabWord")


class UserQuizHistory(Base):
    __tablename__ = 'userquizhistory'
    user_vocab_word_id = Column(Integer, ForeignKey('uservocabwords.id'), primary_key=True)
    quiz_dt = Column(DateTime, primary_key=True)
    hit_or_miss = Column(Boolean)

    user_vocab_word = relationship('UserVocabWord', backpopulates='user_quiz_history')


class UserVocabWord(Base):
    __tablename__ = 'uservocabwords'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    vocab_word_id = Column(Integer, ForeignKey('vocabwords.id'))
    score = Column(Integer)
    notes = Column(String)

    user = relationship('User')
    vocab_word = relationship('VocabWord')
    user_quiz_history = relationship('UserQuizHistory', backpopulates='user_vocab_word')


class Synonym(Base):
    __tablename__ = 'synonyms'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    vocab_words = relationship("SynonymWordAssoc")


class SynonymWordAssoc(Base):
    __tablename__ = 'synonymwordassocs'
    vocab_word_id = Column(Integer, ForeignKey('vocabwords.id'), primary_key=True)
    synonym_id = Column(Integer, ForeignKey('synonyms.id'), primary_key=True)

    synonym_score = Column(Integer)
    notes = Column(String)

    vocab_word = relationship("VocabWord")


class VocabSource(Base):
    __tablename__ = 'vocabsources'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    vocab_words = relationship("VocabSourceWordAssoc")


class VocabSourceWordAssoc(Base):
    __tablename__ = 'vocabsourcewordassocs'
    vocab_word_id = Column(Integer, ForeignKey('vocabwords.id'), primary_key=True)
    vocab_source_id = Column(Integer, ForeignKey('vocabsources.id'), primary_key=True)

    vocab_word = relationship("VocabWord")


class UserVocabSource(Base):
    __tablename__ = 'uservocabsources'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    vocab_source_id = Column(Integer, ForeignKey('vocabsources.id'), primary_key=True)
    score = Column(Integer)

    user = relationship("User")
    vocab_source = relationship("VocabSource")


class UserVocabTag(Base):
    __tablename__ = 'uservocabtags'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)

    vocab_words = relationship("VocabTagWordAssoc")


class VocabTagWordAssoc(Base):
    __tablename__ = 'vocabtagwordassocs'
    vocab_word_id = Column(Integer, ForeignKey('vocabwords.id'), primary_key=True)
    user_vocab_tag_id = Column(Integer, ForeignKey('uservocabtags.id'), primary_key=True)
    subtag = Column(String)

    vocab_word = relationship("VocabWord")



## duplicate for word tags

## duplicate for confusion groups

## duplicate for suffix?


## alternately, allow lists of lists --nah


#Base.MetaData.create_all()
#User.__table__.create(engine?)

