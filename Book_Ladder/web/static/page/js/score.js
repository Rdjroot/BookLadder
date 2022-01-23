//评分分布图模块
    //实例化对象
    var myChart = echarts.init(document.querySelector
    (".page1"));
    //指定配置项和数据
    dataAxis = ['点', '击', '柱', '子', '或', '者', '两', '指', '在', '触', '屏', '上', '滑', '动', '能', '够', '自', '动', '缩', '放'];
    var data = [220, 182, 191, 234, 290, 330, 310, 123, 442, 321, 90, 149, 210, 122, 133, 334, 198, 123, 125, 220];
    var yMax = 500;
    var dataShadow = [];

    for (var i = 0; i < data.length; i++) {
        dataShadow.push(yMax);
    }
    var option = {
        title: {
            text: '核心书籍评分分布',
            textStyle:{color : '#778CDD'},
            subtext: 'The distribution of core book ratings',
            subtextStyle:{color:'#aaa'}
        },
        xAxis: {
            data: dataAxis,
            axisLabel: {
                interval:0,
                width:10,
                overflow:'break',
                inside: true,
                textStyle: {
                    color: '#fff'
                }
            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
            z: 10
        },
        yAxis: {
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                textStyle: {
                    color: '#999'
                }
            }
        },
        dataZoom: [
            {
                type: 'inside'
            }
        ],
        series: [
            {
                type: 'bar',
                showBackground: true,
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(
                        0, 0, 0, 1,
                        [
                            {offset: 0, color: '#ff6633'},
                            {offset: 0.5, color: '#FF5555'},
                            {offset: 1, color: '#FF3333'}
                        ]
                    )
                },
                emphasis: {
                    itemStyle: {
                        color: new echarts.graphic.LinearGradient(
                            0, 0, 0, 1,
                            [
                                {offset: 0, color: '#A9E085'},
                                {offset: 0.7, color: '#83D34E'},
                                {offset: 1, color: '#61B12C'}
                            ]
                        )
                    }
                },
                data: data
            }
        ]
    };

// Enable data zoom when user click bar.
    var zoomSize = 6;
    myChart.on('click', function (params) {
        console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
        myChart.dispatchAction({
            type: 'dataZoom',
            startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
            endValue: dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
        });
    });

    myChart.setOption(option);
