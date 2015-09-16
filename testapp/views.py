from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
def index(request):
    context = {
        'pagetitle': 'robs homepage',
        'pagecontent': 'blah blah blah',
    }
    return render(request, "p_template.html", context)


def vote(request, id):
    return HttpResponse("voted for " + id)


def votepage(request):
    return render(request, "p_formpage.html")


def team(request):
    return render(request, "team.html")


def sigmaexample(request):
    return render(request, "p_sigmaexample.html")


def arcticexample(request):
    return render(request, "p_arcticexample.html")


def crossFilterExample(request):
    return render(request, "p_crossfilterdemo_part2.html")


def demoExamples(request):
    return render(request, "p_feasibilitydemo.html")


def igraphExample(request):
    return render(request, "index.html")


def fetchdata(request, datafile):
    return render(request, "datatemplate.html", datafile=datafile)


def jq(request):
    return render(request, "p_jquerytest.html")


def chord_example(request):
    return render(request, "p_chord_example.html")


def chord(request):
    return render(request, "p_chord.html")


def netflow(request):
    return render(request, "p_netflow_barcharts.html")


def mycrossfilter(request):
    return render(request, "p_mycrossfilter.html")


def mydcseries(request):
    return render(request, "p_dc_myseries.html")


def dcseries(request):
    return render(request, "p_dc_series_example.html")


def d3tut(request, part):
    if part == '1':
        return render(request, "p_d3tut.html")
    elif part == '2':
        return render(request, "p_d3tut_part2.html")
    elif part == '3':
        return render(request, "p_d3tut_part3.html")
    elif part == '4':
        return render(request, "p_d3tut_part4.html")
    elif part == '5':
        return render(request, "p_d3tut_part5.html")
    elif part == 'gbuilder':
        return render(request, "p_graphbuilder.html")
    elif part == 'graph1':
        return render(request, "p_myfirstd3graph.html")
    else:
        return HttpResponse("None Found")


def http404(request):
    return render(request, Http404("No page exists."))
