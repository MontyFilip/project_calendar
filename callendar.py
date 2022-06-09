# wypisanie danych
from abc import ABC


text_entry = """
BEGIN: VCALENDAR
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/Warsaw
X-LIC-LOCATION: Europe/Warsaw
END:TIMEZONE"""
text_end = "\nEND:VCALENDAR"



def list_calendar(strategy, events):
    formated_data = strategy.format(events)
    print(formated_data)

#abstractClass - https://docs.python.org/3/library/abc.html
class ListingStrategy(ABC):
    def format(self, calendar_data):
        pass

# formatowanie wydarzeń do klasycznego formatu

#okropne formatowanie - mozna uzyc fstringa, nie mieszamy
class SimpleListingStrategy(ListingStrategy):
    def format(self, calendar_data):
        data = "".join([self.format_event(event) for event in calendar_data])
        return "    --wydarzenia:-- \n{}".format(data)

    def format_event(self, event):
        return"""
Tytuł: {}
Date: {}, {}\n""".format(event.title,
                       event.date.strftime('%d.%m.%Y'),
                       event.time.strftime('%H:%M'))


# formatowanie wydarzeń do formatu iCalendar


#stringi jako constant albo na gore pliku, albo do innego pliku - nie mieszaj bo wyglada zle
#anotowanie typow - brak w calej apce 
class ICalListingStrategy(ListingStrategy):
    def format(self, calendar_data):
        data = "".join([self.format_event(event) for event in calendar_data])
        return "    --iCalendar format--\n {} {}{}\n".format(text_entry, data, text_end)

    def format_event(self, event):
        dt = "{}T{}00".format(
            # convert z obj date na string
            event.date.strftime("%Y%m%d"),
            # convert z obj time na string
            event.time.strftime("%H%M")
        )
        return """
BEGIN:VEVENT
DTSTART:{}
DTEND:{}
SUMMARY:{}
END:VEVENT""".format(dt, dt, event.title)
