# showt
CLI tagviewer for batch audio files, offering a variety of options and formats
        
There are several short (one-letter) options for showt.  Showt does not take long options
        
    '-p' & '-pp' are common options, to make the printout in color, which helps readability a lot
    ',' (comma) separates values below into header or row.  '-ali,dnt' shows artist, album, & discnumber
        in the header, date, tracknumber & title in the rows.  Tracknumber and title always show in rows
    '-h' is very common, to print as much of the infomation in common with all tags in a header
            instead of in rows.  There are several options for controlling the output, which can be
            used with or without the '-h' option.
            '-a' show the artist
            '-b' show the album title
            '-c' composer
            '-C' comment
            '-d' date (or year)
            '-E' shows all items in the tag, but unrecognized items are unformatted
            '-f' controls the length in characters to allow the filename, ie -f30. Default is 20.
            '-g' genre
            '-G' Group files when a value in the header changes. ie on album title or discnumber change
            '-i' discnumber
            '-I' shows some tech info on the tracks at the left column in the rows.
            '-j' justify tracknumbers so all are the same width in digits
            '-t' tracknumber
            '-u' show rows in read sequence (unsorted)
            '-V' venue
        
