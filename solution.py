from optparse import OptionParser


def get_top_sellers_report(min_date="2020-01-01", max_date="2020-06-30", top=3):
    pass


def getOptions():
    parser = OptionParser()
    parser.add_option("-m", "--min_date", dest="min_date", default="2020-01-01", type="string",
                  help="Start date for the retrieved report.")
    parser.add_option("-x", "--max_date", dest="max_date", default="2020-06-30", type="string",
                  help="End date for the retrieved report.")
    parser.add_option("-t", "--top", dest="top", default=3, type="int",
                  help="Number of records per in each reported group.")
    opt, args = parser.parse_args()
    return opt


def main():
    options = getOptions()


if __name__ == '__main__':
    main()
