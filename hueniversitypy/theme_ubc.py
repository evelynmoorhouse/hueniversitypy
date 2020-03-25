def theme_ubc():
    """ 
    Applies a University of British Columbia theme to all subsequential altair plot objects so they are displayed with the UBC visual identity. 
    See the visual identity at https://brand.ubc.ca/guidelines/downloads/ubc-colour-and-fonts/ 
		
    Returns
    -------
    altair plot : altair.vegalite.v4.api.Chart
    an altair plot with the UBC visual identity colour theme applied. 

    Example
    ----------
    >>> from hueniversitypy.theme_ubc import *
    >>> data = pandas.DataFrame({'X': numpy.random.randint(100, size=100), 
                                'Y': numpy.random.randint(100, size=100), 
                                'Cat': [['A', 'B', 'C'][numpy.random.randint(3, size=1)[0]] for i in range(100)]})
    >>> scatterplot = (altair.Chart(data).mark_circle(size=60, opacity=0.5).encode(x='X', y='Y', color='Cat'))
    >>> alt.themes.register('theme_ubc', theme_ubc)
    >>> alt.themes.enable('theme_ubc')
    >>> scatterplot
    """
    # Code attribution: Sergio Sanchez
    # https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602

    # University font
    font = "Arial"
    labelFont = "Arial" 
    
    # Specify colour palette for UBC
    ubc_palette = ['#002145', '#0055B7', '#00A7E1', '#40B4E5', '#6EC4E8', '#97D4E9']

    return {
        "config": {
            # Title font and size
            "title": {
                "fontSize": 18,
                "font": font,
                "anchor": "start", 
                "fontColor": "#000000"
            },
            # Axes font and sizes
            "axisX": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
                "title": "X Axis Title (units)", 
            },
            "axisY": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "titleFont": font,
                "titleFontSize": 12,
                "title": "Y Axis Title (units)", 
            },
            # Add colour palette
            "range": {
                "category": ubc_palette,
            }
        }
    }
