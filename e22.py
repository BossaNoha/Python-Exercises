class Main:
    def converting_time(self, stored_time):
        converted_time = {}
        own_buffer = 0
        if stored_time > 60:
            converted_time["second"], own_buffer = self.convert_secondsminuteshours(stored_time)
        else: converted_time["second"] = stored_time
        if own_buffer > 60:
            converted_time["minute"], own_buffer = self.convert_secondsminuteshours(own_buffer)
        else: converted_time["minute"] = own_buffer
        if own_buffer > 60:
            converted_time["hour"], own_buffer = self.convert_secondsminuteshours(own_buffer)
        else: converted_time["hour"] = own_buffer
        fixing_grammar = self.grammar_correction(converted_time)
        output = self.outputing(converted_time, fixing_grammar)
        return output

    def convert_secondsminuteshours(self, stored_time):#convert to minutes
        converted_seconds = stored_time %60
        own_buffer = stored_time // 60
        return converted_seconds, own_buffer

    def grammar_correction(self, converted_time):
        fixing_grammar = {}
        for type in converted_time:
            if converted_time[type] > 1:
                fixing_grammar[type] = "s"
            else:
                fixing_grammar[type] = ""
        return fixing_grammar

    def outputing(self, converted_time, fixing_grammar):
        output = ""
        for type in converted_time:
            input = output
            output = input + str(converted_time[type]) + " " + type + fixing_grammar[type] + ", "
        return output

main = Main()
own_converter = main.converting_time(3665)
print (own_converter)
