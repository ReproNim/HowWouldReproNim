# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition


class heresthegist(nodes.Admonition, nodes.Element):
    """Custom "heresthegist" admonition for summaries."""


def visit_heresthegist_html(self, node):
    # it is a simple div with a dedicated CSS class assigned
    self.body.append(
        self.starttag(
            node, 'div', CLASS=('admonition ' + 'heresthegist')))
    node.insert(0, nodes.title(
        'first',
        "Here's the gist"))


def depart_heresthegist_html(self, node):
    self.depart_admonition(node)


def visit_heresthegist_latex(self, node):
    self.body.append("""
    \\begin{tcolorbox}[
        enhanced,
        breakable,
        drop lifted shadow,
        sharp corners,
        title=Here's the gist,
        coltitle=dataladgray,
        colbacktitle=dataladblue,
        colframe=dataladblue!70!black,
        fonttitle=\\bfseries]
    """)


def depart_heresthegist_latex(self, node):
    self.body.append('\n\n\\end{tcolorbox}\n')


class HeresTheGist(BaseAdmonition):
    """
    An admonition summarizing the RepoNim lesson.
    """
    node_class = heresthegist


class findoutmore(nodes.container):
    """Custom "findoutmore" container."""
    pass


def visit_findoutmore_html(self, node):
    self.visit_container(node)


def depart_findoutmore_html(self, node):
    self.depart_container(node)


def visit_findoutmore_latex(self, node):
    self.body.append("""
    \\begin{tcolorbox}[
        enhanced,
        breakable,
        drop lifted shadow,
        sharp corners,
        title=Find out more,
        coltitle=dataladgray,
        colbacktitle=dataladyellow,
        colframe=dataladyellow!70!black,
        fonttitle=\\bfseries]
    """)


def depart_findoutmore_latex(self, node):
    self.body.append('\n\n\\end{tcolorbox}\n')


class FindOutMore(BaseAdmonition):
    """findoutmore RST directive

    The idea here is to use an admonition to parse the RST,
    but actually fully replace it afterwards with a custom
    node structure. This is done to be able to replace a
    rather verbose custom markup that was used before in the
    book. Eventually, it may be replaced (in here) with
    something completely different -- without having to change
    content and markup in the book sources.
    """
    node_class = nodes.admonition
    # empty is no allowed
    has_content = True
    # needs at least a one word titel
    required_arguments = 1

    def run(self):
        # this uses the admonition code for RST parsion
        docnodes = super(FindOutMore, self).run()
        # but we throw away the title, because we want to mark
        # it up as a 'header' further down
        del docnodes[0][0]
        # now put the entire admonition structure into a container
        # that we assign the necessary class to make it 'toggle-able'
        # in HTML
        # outer container
        toggle = findoutmore(
            'toogle',
            # header line with 'Find out more' prefix
            nodes.paragraph(
                # place actual admonition title we removed
                # above
                'title', self.arguments[0],
                # add (CSS) class
                classes=['header'],
            ),
            # place the rest of the admonition structure after the header,
            # but still inside the container
            *docnodes[0].children,
            # properly identify as 'findoutmore' to enable easy custom
            # styling, and also tag with 'toggle'. The later is actually
            # not 100% necessary, as 'findoutmore' could get that
            # functional assigned in CSS instead (maybe streamline later)
            classes=['toggle', 'findoutmore'],
        )
        return [toggle]


def setup(app):
    app.add_node(
        heresthegist,
        html=(visit_heresthegist_html, depart_heresthegist_html),
        latex=(visit_heresthegist_latex, depart_heresthegist_latex),
    )
    app.add_directive('heresthegist', HeresTheGist)
    app.add_node(
        findoutmore,
        html=(visit_findoutmore_html, depart_findoutmore_html),
        latex=(visit_findoutmore_latex, depart_findoutmore_latex),
    )
    app.add_directive('findoutmore', FindOutMore)

# vim: set expandtab shiftwidth=4 softtabstop=4 :
