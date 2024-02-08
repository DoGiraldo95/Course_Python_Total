from collections import namedtuple


class FormatosLiquidacion:
    FORMLIQUIDACION_CONSOLIDADA = r'C:\Users\dgiraldo\Documents\git\Course_Python_Total\Dia 9 (Buscador de Objetos)\pythonProject\Liquidacion\formatos\formato_liquidacion_consolidada.xlsx'
    FORMREPOTCONSOLI_DETALLADO = r'C:\Users\dgiraldo\Documents\git\Course_Python_Total\Dia 9 (Buscador de Objetos)\pythonProject\Liquidacion\formatos\formato_liquidacion_consolidada_detallado.xlsx'
    FORMREPOTLIQUIDACION = r'C:\Users\dgiraldo\Documents\git\Course_Python_Total\Dia 9 (Buscador de Objetos)\pythonProject\Liquidacion\formatos\formato_reporte_liquidación.xlsx'
    FORMREPOTLIQUIDACION_DETALLADO = r'C:\Users\dgiraldo\Documents\git\Course_Python_Total\Dia 9 (Buscador de Objetos)\pythonProject\Liquidacion\formatos\formato_reporte_liquidacion_detallada.xlsx'
    FORMVALORTRASLADAR = r'C:\Users\dgiraldo\Documents\git\Course_Python_Total\Dia 9 (Buscador de Objetos)\pythonProject\Liquidacion\formatos\formato_monto_total_ventas_recargas.xlsx'

    @classmethod
    def formatos(cls):
        Archivos = namedtuple('Archivos', 'ConsolidadoDetallado ReportLiquidacion ReportLiquidacionDetallado Liquidacion ValorTrasladar')
        return Archivos(cls.FORMREPOTCONSOLI_DETALLADO, cls.FORMREPOTLIQUIDACION, cls.FORMREPOTLIQUIDACION_DETALLADO, cls.FORMLIQUIDACION_CONSOLIDADA,  cls.FORMVALORTRASLADAR)




