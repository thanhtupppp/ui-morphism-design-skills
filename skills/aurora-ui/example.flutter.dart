import 'package:flutter/material.dart';

class AuroraBackground extends StatelessWidget {
  const AuroraBackground({super.key, required this.child, this.effectsEnabled = true});

  final Widget child;
  final bool effectsEnabled;

  @override
  Widget build(BuildContext context) {
    final reduceMotion = MediaQuery.maybeOf(context)?.disableAnimations ?? false;
    final showEffects = effectsEnabled && !reduceMotion;

    return Stack(
      fit: StackFit.expand,
      children: [
        const ColoredBox(color: Color(0xFF0D1021)),
        if (showEffects)
          const IgnorePointer(
            ignoring: true,
            child: ExcludeSemantics(
              child: DecoratedBox(
                decoration: BoxDecoration(
                  gradient: RadialGradient(
                    center: Alignment(-0.7, -0.8),
                    radius: 1.15,
                    colors: [
                      Color(0xFF6D5DFC),
                      Color(0x3319C6B5),
                      Color(0x00FF6B9A),
                    ],
                    stops: [0.0, 0.52, 1.0],
                  ),
                ),
              ),
            ),
          ),
        child,
      ],
    );
  }
}

class AuroraHeroCard extends StatelessWidget {
  const AuroraHeroCard({super.key, this.onExplore});

  final VoidCallback? onExplore;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 600;
        return Card(
          elevation: 0,
          color: Colors.white.withValues(alpha: 0.94),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(compact ? 18 : 24)),
          child: Padding(
            padding: EdgeInsets.all(compact ? 16 : 24),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  'Create something remarkable',
                  style: (compact ? Theme.of(context).textTheme.headlineSmall : Theme.of(context).textTheme.headlineMedium)?.copyWith(
                        color: const Color(0xFF101426),
                        fontWeight: FontWeight.w800,
                      ),
                ),
                const SizedBox(height: 12),
                const Text(
                  'The Aurora layer adds atmosphere while the content remains stable and readable.',
                  style: TextStyle(color: Color(0xFF526078)),
                ),
                const SizedBox(height: 20),
                FilledButton(
                  onPressed: onExplore,
                  style: FilledButton.styleFrom(minimumSize: const Size(48, 48)),
                  child: const Text('Explore'),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}

class AuroraExample extends StatelessWidget {
  const AuroraExample({super.key, this.effectsEnabled = true, this.onExplore});

  final bool effectsEnabled;
  final VoidCallback? onExplore;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: AuroraBackground(
        effectsEnabled: effectsEnabled,
        child: SafeArea(
          child: LayoutBuilder(
            builder: (context, constraints) {
              final horizontal = constraints.maxWidth < 600 ? 16.0 : 24.0;
              return Center(
                child: Padding(
                  padding: EdgeInsets.all(horizontal),
                  child: AuroraHeroCard(onExplore: onExplore),
                ),
              );
            },
          ),
        ),
      ),
    );
  }
}
