import re
import statistics
import zipfile


class Text:
    def __init__(self, text):
        self.text = text

    def count_sentences(self):
        return self.count_declarative_sentences() + self.count_incentive_sentences() + \
            self.count_interrogative_sentences()

    def count_declarative_sentences(self):
        return len(re.findall(r'\.\W?', self.text))

    def count_interrogative_sentences(self):
        return len(re.findall(r'\?\W?', self.text))

    def count_incentive_sentences(self):
        return len(re.findall(r'!\W?', self.text))

    def calculate_sentence_average_length(self):
        sentences_list = re.split(r'\.\W? |\?\W? |!\W?', self.text)
        word_list = [re.findall(r'\w+', sen) for sen in sentences_list]
        sum_ = 0
        for words in word_list:
            sum_ += sum(len(word) for word in words)
        return sum_ / (len(sentences_list))

    def calculate_word_average_length(self):
        words_list = re.findall(r'\w+', self.text)
        sum_ = 0
        for word in words_list:
            sum_ += len(word)
        return round(sum_/(len(words_list)))

    def calculate_smiles_count(self):
        smile_pattern = re.compile(r'[;:]-*[()\[\]]+')
        smiles = re.findall(smile_pattern, self.text)
        return len(smiles)

    def extract_sentences_with_apostrophes(self):
        sentences = re.findall(r'[А-ЯЁ][^.!?]*\'[^.!?]*[.!?]', self.text)
        return sentences

    def replace_time(self):
        modified_text = re.sub(r'\b((?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?)\b', '(TBD)', self.text)
        return modified_text

    def count_words_ending_with_vowel(self):
        words = re.findall(r'\b\w*[аеёиоуыэюяАЕЁИОУЫЭЫЯ]\b', self.text)
        return len(words)

    def find_average_word_length_in_line(self):
        average_length = self.calculate_word_average_length()
        words = []
        for word in self.text.split():
            if len(word) == average_length:
                words.append(word)
        if words:
            return words
        else:
            string = "Слов длиной " + str(average_length) + " нет в строке"
            return string

    def get_every_fifth_word(self):
        every_fifth_word = []
        for i in range(0, len(self.text.split()), 5):
            every_fifth_word.append(self.text.split()[i])
        return every_fifth_word

    def task(self):
        sentences_count = self.count_sentences()
        interrogative_sentences = self.count_interrogative_sentences()
        declarative_sentences = self.count_declarative_sentences()
        incentive_sentences = self.count_incentive_sentences()
        average_sentence_len = self.calculate_sentence_average_length()
        average_word_len = self.calculate_word_average_length()
        smileys_count = self.calculate_smiles_count()

        sentences_with_apostrophes = self.extract_sentences_with_apostrophes()
        modified_text = self.replace_time()
        words_ending_with_vowel_count = self.count_words_ending_with_vowel()
        average_word_len_in_line = self.find_average_word_length_in_line()
        every_fifth_word = self.get_every_fifth_word()

        task2_results = {
            'Количество предложений в тексте': sentences_count,
            'Количество повествовательных предложений': declarative_sentences,
            'Количество вопросительных предложений': interrogative_sentences,
            'Количество побудительных предложений': incentive_sentences,
            'Средняя длина предложения в символах': average_sentence_len,
            'Средняя длина слова в тексте в символах': average_word_len,
            'Количество смайликов в тексте': smileys_count,

            'Предложения, содержащие апострофы': sentences_with_apostrophes,
            'Текст после замены времени на "(TBD)"': modified_text,
            'Количество слов, заканчивающихся на гласную букву': words_ending_with_vowel_count,
            'Слова длиной n символов в строке': average_word_len_in_line,
            'Каждое пятое слово': every_fifth_word
        }
        return task2_results


def read_from_file(filename):
    f = None
    try:
        f = open(filename, 'r')
        text = f.read()
        return text
    except Exception as e:
        print('error while working with file:', e)
    finally:
        if f:
            f.close()
    return ''


def save_to_zip(result, filename):
    with zipfile.ZipFile(f'{filename}.zip', 'w') as zip_file:
        for key, value in result.items():
            if isinstance(value, list):
                value = '\n'.join(value)
            zip_file.writestr(key + '.txt', str(value))


def write_to_file(text, filename):
    f = None
    try:
        f = open(filename, 'w')
        f.write(text)
    except Exception as e:
        print('error while working with file:', e)
    finally:
        if f:
            f.close()


def task2():
    while True:
        choice = int(input('Please, choose option:\n'
                            '1: test1\n'
                            '2: test2\n'
                            '3: test3\n'
                            '4: input\n'
                            '0: exit\n'))
        match choice:
            case 1:
                text = Text(read_from_file('test1.txt'))
                result = text.task()
                save_to_zip(result, 'output1')
                for key, value in result.items():
                    print(key, ' : ', value)
            case 2:
                text = Text(read_from_file('test2.txt'))
                result = text.task()
                save_to_zip(result, 'output2')
                for key, value in result.items():
                    print(key, ' : ', value)
            case 3:
                text = Text(read_from_file('test3.txt'))
                result = text.task()
                save_to_zip(result, 'output3')
                for key, value in result.items():
                    print(key, ' : ', value)
            case 4:
                text = Text(input("please input string: "))
                string = text.text
                result = text.task()
                save_to_zip(result, 'output4')
                for key, value in result.items():
                    print(key, ' : ', value)

            case 0:
                break
            case _:
                print('please choose from 0 to 3:')
                continue

