import datetime
from optparse import OptionParser
from brandAdapter import BrandAdapter
from cityAdapter import CityAdapter
from productAdapter import ProductAdapter
from salesAdapter import SalesAdapter
from storeAdapter import StoreAdapter

default_top = 3
default_min_date = "2020-01-01"
default_max_date = "2020-06-30"


def get_formatted_report(productDf, storeDf, brandDf, cityDf):

    return '-- top seller product --\n' + productDf.to_string(index=False) + '\n'\
    '-- top seller store --\n' + storeDf.to_string(index=False) + '\n'\
    '-- top seller brand --\n' + brandDf.to_string(index=False) + '\n'\
    '-- top seller city --\n' + cityDf.to_string(index=False)



def generate_top_sellers_report(min_date=default_min_date, max_date=default_max_date, top=default_top):
    salesAdapter = SalesAdapter().between(min_date, max_date)
    productAdapter = ProductAdapter(salesAdapter.get_products())
    storeAdapter = StoreAdapter(salesAdapter.get_stores())
    brandAdapter = BrandAdapter(productAdapter.get_brands())
    cityAdapter = CityAdapter(storeAdapter.get_cities())

    return get_formatted_report(
        productAdapter.get_top_seller_report(top),
        storeAdapter.get_top_seller_report(top),
        brandAdapter.get_top_seller_report(top),
        cityAdapter.get_top_seller_report(top)
    )



def validateOptions(opt):
    try:
        datetime.datetime.strptime(opt.min_date, '%Y-%m-%d')
        datetime.datetime.strptime(opt.max_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, dates should be YYYY-MM-DD")
    if not isinstance(opt.top, int) or opt.top < 0:
        raise ValueError("Incorrect data format, top should be positive integer")

    return opt


def getOptions():
    parser = OptionParser()
    parser.add_option("-m", "--min-date", dest="min_date", default=default_min_date, type="string",
                      help="Start date for the retrieved report.")
    parser.add_option("-x", "--max-date", dest="max_date", default=default_max_date, type="string",
                      help="End date for the retrieved report.")
    parser.add_option("-t", "--top", dest="top", default=default_top, type="int",
                      help="Number of records per in each reported group.")
    opt, args = parser.parse_args()
    return validateOptions(opt)


def main():
    options = getOptions()
    output = generate_top_sellers_report(options.min_date, options.max_date, options.top)

    print(output)


if __name__ == '__main__':
    main()
