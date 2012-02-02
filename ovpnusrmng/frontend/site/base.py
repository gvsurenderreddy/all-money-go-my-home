from settings import SITENAME, SITEMOTTO

sitebase={
    'SITENAME': SITENAME,
    'SITEMOTTO': SITEMOTTO,
}

def joinbase(context):
    ret=context.copy()
    ret.update(sitebase)
    return ret